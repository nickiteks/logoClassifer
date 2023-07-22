import { Block1 } from './Block1'
import { Header } from './Header'
import { Block2 } from './Block2'
import './Home.css'

export const Home = () => {

    return(
        <div className="home">
            <Header/>
            <Block1/>
            <Block2/>
        </div>
    )
}