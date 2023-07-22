import './Header.css'
import Icon from '../images/header/IconHeader.svg'
import { Button, ButtonSize, ButtonType } from '../components/button/Button'

export const Header = () => {

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
            />
        </div>
    )
}