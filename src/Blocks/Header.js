import './Header.css'
import { useState } from 'react'
import RegistrationModal from '../components/RegistationModal'
import Icon from '../images/header/IconHeader.svg'
import { Button, ButtonSize, ButtonType } from '../components/button/Button'

export const Header = () => {

    const [isModalOpen, setIsModalOpen] = useState(false);

    const handleOpenModal = () => {
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
    };

    return(
        <div className="header">
            <img src={Icon}></img>
            <div className="header-title">Taganrogky</div>
            <div className="header-text">Начать</div>
            <div className="header-text">Как это работает</div>
            <div className="header-text">Сотрудничество</div>
            <div className="header-text">Партнеры</div>
            <Button 
                type={ButtonType.PRIMARY} 
                size={ButtonSize.SMALL}
                text={"Вход/Регистрация"}
                round
                onClick={handleOpenModal}
            />
            <RegistrationModal isOpen={isModalOpen} onClose={handleCloseModal} />
        </div>
    )
}