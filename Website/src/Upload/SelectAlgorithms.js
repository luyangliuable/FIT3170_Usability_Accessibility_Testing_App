import React from 'react'
import { Container } from "react-bootstrap";
import { useState } from 'react';

import './Upload.css';
import './accordion.css';

import {
    Accordion,
    AccordionItem,
    AccordionItemHeading,
    AccordionItemButton,
    AccordionItemPanel,
} from 'react-accessible-accordion';

// export default class Upload extends Component {

const SelectAlgorithms = () => {
    const [resultFiles, updateResultFiles] = useState(["./dir_to_file/example_result_file.jpeg"]);
    const [currentAppStatus, updateCurrentAppStatus] = useState("READY");
    var reports = [];  /* TODO link to backend */

    var algorithms = [
        {
            uuid: "gifdroid",
            heading: "GifDroid",
            input: "Video",
            content: "GifDroid does things and requires an additional video input"
        },
        {
            uuid: "venus",
            heading: "Venus",
            input: "-",
            content: "Venus does things and does not require any additional inputs"
        }
    ]

    const [checkedState, setCheckedState] = useState(
        new Array(algorithms.length).fill(false)
    );

    const handleOnChange = (position) => {
        const updatedCheckedState = checkedState.map((item, index) =>
            index === position ? !item : item
        );
        setCheckedState(updatedCheckedState);
    };

    return (
        <Container className='container-nav'>
            <div className="upload-root">

                <p className="upload-text-60 upload-text-center">SELECT ALGORITHMS</p>
                <p className="upload-text-30 upload-text-center">Select which algorithms you want your APK to be assessed by</p>

                <div className="upload-vspacing-40"> </div>

                {/* ============================= */}
                {/* ACCORDIANS FOR EACH ALGORITHM */}
                {/* Store each algorithm as an    */}
                {/* item in an item map           */}
                {/* ============================= */}

                <Accordion allowZeroExpanded allowMultipleExpanded>
                    {algorithms.map((algorithm, index) => (
                        <AccordionItem key={algorithm.uuid}>
                            <AccordionItemHeading>
                                <AccordionItemButton>
                                    <h3> {algorithm.heading} </h3>
                                </AccordionItemButton>
                            </AccordionItemHeading>
                            <AccordionItemPanel>
                                Additional Inputs: {algorithm.input}
                                {algorithm.content}
                            </AccordionItemPanel>
                            {/* <input
                                type="checkbox"
                                id={`custom-checkbox-${index}`}
                                checked={checkedState[index]}
                                onChange={() => handleOnChange(index)}
                            /> */}
                        </AccordionItem>
                    ))}
                </Accordion>

                <div className="upload-vspacing-40"> </div>
            </div>
        </Container>
    );
}

export default SelectAlgorithms;
