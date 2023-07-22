import './Block1.css'
import Icon1 from '../images/block1/CityBG.svg'
import Icon2 from '../images/block1/Img.svg'
import { Button, ButtonSize, ButtonType } from '../components/button/Button'

export const Block1 = () => {

    return(
        <div className="block1">
            <div className="block1-title">Your sity style</div>
            <div className="block1-text">Система экспертных оценок городских вывесок</div>
            <div className="block1-fileblock">
                <img src={Icon2}/>
                <div>Выберете или перетащите файл</div>
                <div className="block1-text2">JPG or PNG, file size no more than 10MB</div>
                <div className="block1-button__style">
                    <Button 
                        type={ButtonType.SECONDARY}
                        size={ButtonSize.MEDIUM}
                        text={"select file"}/>
                    </div>
            </div>
            <img className="block1-icon" src={Icon1}/>
        </div>
    )
}
