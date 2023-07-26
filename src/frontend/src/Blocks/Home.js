import { Block1 } from './Block1'
import { Header } from './Header'
import { Block2 } from './Block2'
import { Block3 } from './Block3'
import './Home.css'

function Home({setPredictionData}){

    return(
        <div className="home">
            <Header/>
            <Block1 setPredictionData={setPredictionData}/>
            <Block2/>
            <Block3/>
        </div>
    )
}

export default Home;