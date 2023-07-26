import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import Icon1 from '../images/block1/CityBG.svg';
import Icon2 from '../images/block1/Img.svg';
import { Button, ButtonSize, ButtonType } from '../components/button/Button';
import axios from 'axios';
import './Block1.css';

export const Block1 = ( {setPredictionData}) => {
    const [selectedFileName, setSelectedFileName] = useState('');
    const fileInputRef = useRef(null);
    const navigate = useNavigate();

    const handleFileChange = async (event) => {
        try {
            const formData = new FormData();
            formData.append('file', event.target.files[0]);
        
            const response = await axios.post('http://127.0.0.1:8000/api/data', formData);
            setPredictionData(response.data)
            navigate('/results');
            } catch (error) {
            console.error('Error:', error);
            }
        };

    const handleButtonClick = () => {
        fileInputRef.current.click();
    };

    const handleFileNameDisplay = (event) => {
        setSelectedFileName(event.target.value.split('\\').pop());
    };

    return (
        <div className="block1">
            <div className="block1-title">Стиль твоего города </div>
            <div className="block1-text">Система экспертных оценок городских вывесок</div>
            <div className="block1-fileblock">
                <img src={Icon2} alt="File Icon" />
                <div className='block1-text1'>Выберете или перетащите файл</div>
                <div className="block1-text2">JPG or PNG, file size no more than 10MB</div>
                <div className="block1-button__style">
                    <Button type={ButtonType.SECONDARY} size={ButtonSize.MEDIUM} text="Select file" onClick={handleButtonClick} />
                    <input
                        type="file"
                        ref={fileInputRef}
                        style={{ display: 'none' }}
                        onChange={(e) => {
                            handleFileChange(e);
                            handleFileNameDisplay(e);
                        }}
                    />
                </div>
                {selectedFileName && <div>Выбранный файл: {selectedFileName}</div>}
            </div>
            <img className="block1-icon" src={Icon1} alt="City Icon" />
        </div>
    );
};