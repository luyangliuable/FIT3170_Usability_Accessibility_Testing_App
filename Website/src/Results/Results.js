import React, { useState } from 'react'

import "./Results.css"

import ReportsTable from "../Results/components/ReportsTable"

// export default class Results extends Component {
const Results = () => {

    /* TODO link to backend */
    const [reports, updateReport] = useState([
        { "image": "https://i.ibb.co/r5fN6X2/a2dp-Vol-App-Chooser.png", "issues": ["This item may not have a label readable by screen readers", "The item's text contrast ratio is 1.99. This ratio is based on an estimated foreground color of #B4B4B4 and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "This item's height is 45dp. Consider making the height of this touch target 48dp or larger."], "app": "xbot" },
        { "image": "https://i.ibb.co/gVfKbY8/a2dp-Vol-Custom-Intent-Maker.png", "issues": ["This item may not have a label readable by screen readers.", "This item may not have a label readable by screen readers.", "The item's text contrast ratio is 1.23. This ratio is based on an estimated foreground color of #E3E3E3 and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "This item's height is 45dp. Consider making the height of this touch target 48dp or larger.", "This item's height is 45dp. Consider making the height of this touch target 48dp or larger.", "This item's height is 45dp. Consider making the height of this touch target 48dp or larger."], "app": "xbot"},

        { "image": "https://i.ibb.co/B4ZLx6B/a2dp-Vol-main.png", "issues": ["The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.",  "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater." , "The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater.", "this item's size is 32dp x 32dp. consider making this touch target 48dp wide and 48dp high or larger.", "this item's size is 32dp x 32dp. consider making this touch target 48dp wide and 48dp high or larger.", "this item's size is 32dp x 32dp. consider making this touch target 48dp wide and 48dp high or larger.", "This clickable item's speakable text: Not checked is identical to that of 9 other item(s)."], "app": "xbot"},

        {"image": "https://i.ibb.co/87WNssZ/a2dp-Vol-Provider-List.png", "issues": ["The item's text contrast ratio is 1.04. This ratio is based on an estimated foreground color of #FFFFFF and an estimated background color of #FAFAFA. Consider increasing this item's text contrast ratio to 3.00 or greater."],
         "app": "xbot",
        },
        { "image": "https://i.ibb.co/Wk0dpQH/a2dp-Vol-App-Chooser.jpg", "issues": [], "app": "owleye" }, { "image": "https://i.ibb.co/XFRt8xf/a2dp-Vol-Custom-Intent-Maker.jpg", "issues": [], "app": "owleye" }, { "image": "https://i.ibb.co/jry5kyv/a2dp-Vol-main.jpg", "issues": [], "app": "owleye" }, { "image": "https://i.ibb.co/7p5dwvb/a2dp-Vol-Packages-Chooser.jpg", "issues": [], "app": "owleye" }, { "image": "https://i.ibb.co/tzG58DV/a2dp-Vol-Provider-List.jpg", "issues": [], "app": "owleye" }
    ]);

    const [images, updateImages] = useState([
        ["test_file.apk", "100 mb", "21/04/22", "https://ourwebsite.com.au/results/dummyid1"],
        ["test_file2.apk", "150 mb", "21/04/22", "https://ourwebsite.com.au/results/dummyid2"],
        ["test_file3.apk", "60 mb", "20/04/22", "https://ourwebsite.com.au/results/dummyid3"]
    ]);

    return (
            <div style={{display: 'flex', justifyContent:"center", flexDirection: "column", position: "absolute", width: "80%", left: "10%", top: "10%", padding: "10px"}}>
            {
                reports.map(report => (
                    <>
                        <ReportsTable issues={report["issues"]} image={report['image']} app={report['app']}/>
                    </>
                ))
            }
        </div>
    );
};





export default Results;
