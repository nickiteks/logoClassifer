import './Block1.css';
import Icon1 from '../images/block1/CityBG.svg';
import Icon2 from '../images/block1/Img.svg';
import { Button, ButtonSize, ButtonType } from '../components/button/Button';
import axios from 'axios';
import { useState } from 'react';

export const Block1 = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState('');

  const handleFileChange = async (event) => {
    // ...
    try {
      const formData = new FormData();
      formData.append('file', event.target.files[0]);

      const response = await axios.post('http://127.0.0.1:8000/results/', formData);
      const data = response.data;
      setPrediction(data.Predict);
    } catch (error) {
      console.error('Error:', error);
    }
  };
  

//   const handleUpload = () => {
//     const formData = new FormData();
//     formData.append('file', selectedFile);

//     axios.post('http://your-django-server-url/upload/', formData)
//       .then((response) => {
//         // Обработка успешного ответа от сервера, если необходимо
//       })
//       .catch((error) => {
//         // Обработка ошибки при запросе, если необходимо
//       });
//   };


  return (
    <div className="block1">
      <div className="block1-title">Your sity style</div>
      <div className="block1-text">Система экспертных оценок городских вывесок</div>
      <div className="block1-fileblock">
        <img src={Icon2} alt="File Icon" />
        <div>Выберете или перетащите файл</div>
        <div className="block1-text2">JPG or PNG, file size no more than 10MB</div>
        <div className="block1-button__style">
          <Button type={ButtonType.SECONDARY} size={ButtonSize.MEDIUM} text="select file" />
          <input type="file" onChange={handleFileChange} />
        </div>
        {prediction && <div>Предсказание: {prediction}</div>}
      </div>
      <img className="block1-icon" src={Icon1} alt="City Icon" />
    </div>
  );
};