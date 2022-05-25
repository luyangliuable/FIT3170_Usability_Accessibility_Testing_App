from flask import Flask
from flask import render_template, Blueprint, jsonify, request, Response, send_file, redirect, url_for
from server.distiller.code. run_storydistiller import *
import os
import pymongo

from server.models.User import *

distiller_blueprint = Blueprint('distiller', __name__)

@login_blueprint.route('/')
def distiller():
    if main_folder is not None:
        output = main_folder
    else:
        output = sys.argv[1] # Main folder path
    # output = '/home/senchen/Engines/StoryDistiller/main-folder/'
    # output = '/Users/chensen/Tools/storydistiller/'
    # output = '/Users/chensen/Tools/storydistiller/'
    # output = sys.argv[2]
    # adb = sys.argv[2] # adb emulator


    apk_dir = os.path.join(output, 'apks/') # APK folder

    out_csv = os.path.join(output, 'log.csv') # Log file

    ###############################################################################
    #                         Display environment details                         #
    ###############################################################################

    print "output directory (main folder): " + output
    print "apk directory:" + apk_dir
    print "out_csv:" + out_csv
    print "adb: " + adb

    print "java home path: " + str(java_home_path)
    print "sdk platform path" + str(sdk_platform_path)
    print "lib_home_path" + str(lib_home_path)
    print "callbacks path" + str(callbacks_path)
    print "jadx path" + str(jadx_path)
    print "ic3 path" + str(ic3_path)

    csv.writer(open(out_csv, 'a')).writerow(('apk_name', 'pkg_name', 'all_act_num', 'launched_act_num',
                                             'act_not_in_atg', 'act_not_launched', 'all_atg', 'soot_atg', 'new_atg'))

    # print 'All atgs: ' + str(len(union_list))
    # print union_list
    # print 'Soot atgs: ' + str(len(static_list))
    # print static_list
    # print 'New atgs: ' + str(len(new_unique_list))
    # print new_unique_list
    # print 'New edges: ' + str(len(new_edge_list))
    # print new_edge_list

    for apk in os.listdir(apk_dir):
        if apk.endswith('.apk'):

            root = adb + '-s %s root'%(emulator)  # root the emulator before running
            print commands.getoutput(root)

            apk_path = apk_dir + apk
            org_apk_name = apk.split('.apk')[0]

            print 'apk path: ' + apk_path
            print '[1] Start to rename the app and get package name.'
            apk_path = rename(apk_path, apk_dir)
            apk_name = os.path.split(apk_path)[1].split('.apk')[0]
            print '[1] Rename app is done.'

            '''
            Create output folder
            '''
            dir = output + '/outputs/' + apk_name + '/'
            if not os.path.exists(dir):
                os.makedirs(dir)

            '''
            Save pkg name
            '''
            open(dir + 'used_pkg_name.txt', 'wb').write(used_pkg_name + '\n')
            open(dir + 'defined_pkg_name.txt', 'wb').write(defined_pkg_name + '\n')

            '''
            Create sootOutput folder
            '''
            sootOutput_dir = output + 'sootOutput/' + apk_name + '/'
            if not os.path.exists(sootOutput_dir):
                os.makedirs(sootOutput_dir)

            print '[2] Start to decompile apk.'
            decompile(apk_path, apk_name)
            print '[2] Decompile apk is done.'

            '''
            The results are used for running IC3, which are the inputs of IC3
            '''
            print 'Start to get SootOutput (class) and check layout type'
            getSootOutput(apk_path, apk_name)

            print '[3] Start to run IC3 ' + apk_name
            results_IC3 = run_IC3(apk_path)
            print '[3] Run IC3 is done.'

            print '[4] Start to parse IC3.'
            dict = parse_IC3(results_IC3, used_pkg_name) # will check whether is defined_pkg_name
            save_parsed_IC3(dict)
            print '[4] Parse the result of IC3 is done.'

            print '[5] Start to get call graphs ' + apk_name
            CG_path = output + 'soot_cgs/'
            if not os.path.exists(CG_path):
                os.makedirs(CG_path)
            results_CG = CG_path + apk_name + '.txt'
            if not os.path.exists(results_CG):
                get_callgraphs(apk_path)
            print '[5] Get call graphs is done.'

            print '[6] Start to parse call graphs ' + apk_name
            dict = parse_CG(results_CG, used_pkg_name)
            save_parsed_CG(dict)
            print '[6] Parse call graphs is done'

            print '[7] Get JIMPLE ' + apk_name
            shutil.rmtree(sootOutput_dir)  # Delete sootOutput
            #os.chdir(output + 'apktojimple')
            #os.system('./decompile.sh %s %s'%(apk_path, sootOutput_dir))
            #print '[7] Get Jimple is done'

            print '[8] Start to get ATG ' + apk_name
            print 'soot pkg: ' + used_pkg_name
            run_soot(output, apk_path, used_pkg_name, apk_name)
            get_atgs(apk_name)
            print '[8] Get ATGs is done'

            print '[9] Start to get corresponding appstory ' + apk_name
            results_JavaCode = output + 'java_code/' + apk_name + '/'
            result_apkfolder = output + 'outputs/' + apk_name + '/'
            results_visulization_ICCs = result_apkfolder + apk_name + '_atgs.txt'

            # copy apk_name + '_atgs' as apk_name + '_atgs_static'
            results_visulization_ICCs_static = result_apkfolder + apk_name + '_atgs_static.txt'
            if os.path.exists(results_visulization_ICCs):
                os.system('cp %s %s' % (results_visulization_ICCs, results_visulization_ICCs_static))



            processed_cg_file = result_apkfolder + apk_name + '_cgs.txt'
            if os.path.exists(results_JavaCode):
                get_act_method_code.main(results_JavaCode, result_apkfolder, results_visulization_ICCs, processed_cg_file, launchActivity)
            print '[9] Get components and method code is done'

            print '[10] Start to get method call sequence'
            if os.path.exists(processed_cg_file):
                traverse_tree.main(processed_cg_file, results_visulization_ICCs, result_apkfolder)
            print '[10] Get method call sequence is done'

            ####Core####
            print '[11] Get the screenshots ' + apk_name
            if not os.path.exists(result_apkfolder + 'screenshots'):
                os.mkdir(result_apkfolder + 'screenshots')

            # 00 appstory
            all_acts = run_rpk_explore_apk.execute(apk_path, apk_name, result_apkfolder, output)
            print '[11] Get the screenshots is done'

            union_list = []
            static_list = []
            new_unique_list = []
            ###parse static and dynamic atgs
            dynamic_explore_result = os.path.join(result_apkfolder, apk_name + '_atgs_dynamic.txt')

            #union_list, static_list, new_unique_list, new_edge_list = parse(dir, results_visulization_ICCs, dynamic_explore_result)

            # print 'All atgs: ' + str(len(union_list))
            # print union_list
            # print 'Soot atgs: ' + str(len(static_list))
            # print static_list
            # print 'New atgs: ' + str(len(new_unique_list))
            # print new_unique_list
            # print 'New edges: ' + str(len(new_edge_list))
            # print new_edge_list

            if all_acts != None:
                # Get some statistics
                launched_act_num = int(
                    commands.getoutput('ls %s | wc -l' % (result_apkfolder + 'screenshots')).split('\n')[0])

                # Print launched_act_num
                act_not_in_atg = get_act_not_in_atg(all_acts)

                # Print act_not_in_atg
                act_not_launched = get_acy_not_launched(all_acts)

                # Print act_not_launched
                csv.writer(open(out_csv, 'a')).writerow((apk_name, used_pkg_name, len(all_acts), launched_act_num, act_not_in_atg, act_not_launched,
                                                         str(len(union_list)), str(len(static_list)), str(len(new_unique_list))))

            # if _atg_dynamic exist, copy it to _atgs
            results_visulization_ICCs_dynamic = result_apkfolder + apk_name + '_atgs_dynamic.txt'
            if os.path.exists(results_visulization_ICCs_dynamic):
                lines = open(results_visulization_ICCs_dynamic, 'r').readlines()
                for line in lines:
                    open(results_visulization_ICCs, 'ab').write(line.split('->')[0] + '-->' + line.split('->')[-1])

            ####HTML, Webpage generation####
            print '[12] Get Json'
            config_path = os.path.join(output, 'config/')
            copy_search_file(os.path.join(config_path, 'template/'), os.path.join(result_apkfolder, 'output/'))
            create_json_withindent.execute(result_apkfolder)
            print '[12] Get Json: DONE'

            os.remove(os.path.join(result_apkfolder, apk_name + '.apk'))
            os.remove(apk_path)



@login_blueprint.route('/signUp', methods=['POST'])
def signUpUser():
    return UserModel().signUpUser()


@login_blueprint.route('/login', methods=['POST'])
def loginUser():
    return UserModel().loginUser()


if __name__ == "__main__":
    pass
    # login_blueprint.run(host="0.0.0.0", port=5002, debug=True)
