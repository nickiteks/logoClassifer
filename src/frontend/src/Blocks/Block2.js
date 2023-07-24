import './Block2.css'
import { Button, ButtonSize, ButtonType } from '../components/button/Button'
import Icon1 from '../images/block2/pseudo.svg'
import Icon2 from '../images/block2/using-software.svg'
import Icon3 from  '../images/block2/pseudo (1).svg'
import Icon4 from '../images/block2/img (1).svg'
import Icon5 from '../images/block2/img (2).svg'

export const Block2 = () => {

    const handleLinkClick1 = () => {
        window.location.href = "https://pytorch.org/"
    }

    const handleLinkClick2 = () => {
        window.location.href = "https://link.springer.com/article/10.1007/s00362-023-01437-w"
    }

    const handleLinkClick3 = () => {
        window.location.href = "https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/innovate/best-practices/predict"
    }

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
                        <Button
                        onClick={handleLinkClick1}
                        type={ButtonType.PRIMARY} 
                        size={ButtonSize.LARGE} 
                        text={"LEARN MORE"} 
                        round/>
                    </div>
                </div>
            </div>

            <img src={Icon3}/>

            <div className="block2-wrapper">
                <div className="block2-list__wrapper">
                    <div className="block2-title">Анализ дизайна на обученных данных</div>
                    <div className="block2-text">
                        Пользователь может загрузить изображение с дизайном для оценки нейросетью по специально обученному алгоритму
                    </div>
                    <div className="block2-button__style">
                        <Button
                        onClick={handleLinkClick2}
                        type={ButtonType.PRIMARY} 
                        size={ButtonSize.LARGE} 
                        text={"LEARN MORE"} 
                        round/>
                    </div>
                </div>
                <img className="block2-icon" src={Icon4}/>
            </div>

            <img src={Icon1}/>

            <div className="block2-wrapper">
                <img className="block2-icon" src={Icon5}/>
                <div className="block2-list__wrapper">
                    <div className="block2-title">Получение рекомендаций</div>
                    <div className="block2-text">
                        Система выдаёт результаты оценки дизайна по различным критериям и даёт рекомендации по его улучшению
                    </div>
                    <div className="block2-button__style">
                        <Button 
                        onClick={handleLinkClick3}
                        type={ButtonType.PRIMARY} 
                        size={ButtonSize.LARGE} 
                        text={"LEARN MORE"} 
                        round/>
                    </div>
                </div>
            </div>


        </div>
    )
}
