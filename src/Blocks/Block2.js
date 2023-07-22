import './Block2.css'
import { Button, ButtonSize, ButtonType } from '../components/button/Button'
import Icon1 from '../images/block2/pseudo.svg'
import Icon2 from '../images/block2/using-software.svg'
import Icon3 from  '../images/block2/pseudo (1).svg'

export const Block2 = () => {

    return(
        <div className="block2">
            <img src={Icon1}/>
            <div className="block2-wrapper">
                <img className="block2-icon" src={Icon2}/>
                <div className="block2-list__wrapper">
                    <div className="block2-title">Обучение нейросети</div>
                    <div className="block2-text">Нейросеть была обучена на большом 
                            количестве данных о визуальном 
                            оформлении успешных компаний, а так же 
                            принципах приятного и продающего дизайна
                    </div>
                    <div className="block2-button__style">
                        <Button type={ButtonType.PRIMARY} 
                        size={ButtonSize.LARGE} 
                        text={"LEARN MORE"} 
                        round/>
                    </div>
                </div>
            </div>
            <img src={Icon3}/>
        </div>
    )
}
