import './RegistationModal.css'
import { useState } from 'react';

const RegistrationModal = ({ isOpen, onClose }) => {
    const [phoneNumber, setPhoneNumber] = useState('');
    const [fullName, setFullName] = useState('');

    const handlePhoneNumberChange = (event) => {
        setPhoneNumber(event.target.value);
    };

    const handleFullNameChange = (event) => {
        setFullName(event.target.value);
    };

    const handleSubmit = () => {
        // Здесь вы можете обрабатывать данные формы регистрации, например, отправлять на сервер
        console.log('Номер телефона:', phoneNumber);
        console.log('Имя и фамилия:', fullName);
        // После обработки данных, можно закрыть модальное окно
        onClose();
    };

    if (!isOpen) return null;

    return (
        <div className="modal">
        <div className="modal-content">
            <h2>Регистрация</h2>
            <input
            type="text"
            placeholder="Номер телефона"
            value={phoneNumber}
            onChange={handlePhoneNumberChange}
            />
            <input
            type="text"
            placeholder="Имя и фамилия"
            value={fullName}
            onChange={handleFullNameChange}
            />
            <button onClick={handleSubmit}>Зарегистрироваться</button>
            <button onClick={onClose}>Закрыть</button>
        </div>
        </div>
    );
};

export default RegistrationModal;
