import './Block3.css'
import Icon1 from '../images/block3/Group 23 (1).svg'
import Icon2 from '../images/block3/Frame.svg'
import Icon3 from '../images/block3/Frame (1).svg'
import Icon4 from '../images/block3/VK.svg'
import Icon5 from '../images/block3/Instagram.svg'
import Icon6 from '../images/block3/Youtube.svg'
import Icon7 from '../images/block3/Telegram.svg'
import Icon8 from '../images/block3/image 8.svg'
import Icon9 from '../images/block3/image 9.svg'
import Icon10 from '../images/block3/Group 24.svg'

export const Block3 = () => {

    return(
        <div className="block3">
            <div className='line'></div>
            <div className='block3-list__wrapper'>
                <div className='block3-list'>
                    <div className='block3-wrapper__rows'>
                        <img src={Icon1}/>
                        <div className='block3-title'>Taganrogky</div>
                    </div>
                    <div className='block3-text1'>Проект команды Таганрожки {"\n"} 
                    Летней школы ИИ 2023, {"\n"}
                    г. Таганрог</div>
                </div>

                <div className='block3-list'>
                    <div className='bblock3-wrapper__rows'>
                        <img src={Icon2}/>
                        <div className='block3-text1'>(021) 111-222-333-44</div>
                    </div>
                    <div className='block3-wrapper__rows'>
                        <img src={Icon3}/>
                        <div className='block3-text1'>taganrogky@gmail.com</div>
                    </div>
                </div>

                <div className='block3-list'>
                    <div className='block3-text2'>Follow us</div>
                    <div className='block3-wrapper__rows'>
                        <img src={Icon4}/>
                        <img src={Icon5}/>
                        <img src={Icon6}/>
                        <img src={Icon7}/>
                    </div>
                </div>
            </div>
            <div className='line'></div>
            <div className='block3-list__wrapper'>
                <div className='block3-text2'> Taganrogky | All Rights Reserved.</div>
                <img src={Icon8}/>
                <img src={Icon9}/>
                <div className='block3-text2'>Terms Of Service | Privacy Policy | Help</div>
            </div>
            <div className='block3-icon__wrapper'>
                <img className='block3-icon' src={Icon10}/>
            </div>
        </div>
    )
}