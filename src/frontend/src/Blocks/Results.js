/* eslint-disable jsx-a11y/img-redundant-alt */
import "./Results.css";
import { Card, CardType, CardWrapper } from "../components/cards/Card";
import { Header } from "./Header";
import DoughnutChart from "./DoughnutChart";
import { Button, ButtonSize, ButtonType } from "../components/button/Button";
import Icon1 from '../images/results/Logo.svg'
import Icon2 from '../images/results/Logo (1).svg'
import Icon3 from '../images/results/BG image (3) 1.svg'

function Results({ predictionData }) {
  const { file, Style, Noice, Place } = predictionData;

  const handleLinkClick4 = () => {
    window.location.href = "https://u-dm.ru/o_nas.html"
}

const handleLinkClick5 = () => {
  window.location.href = "http://iceberg.group/"
}

  const elements = [
    {
      chart:<DoughnutChart value={Style} color={"#C2CDFF"}/>,
      text: <div className="card-text"><b>Стиль</b> - визуальная привлекательность вывески, без учёта среды</div>,
    },
    {
      chart:<DoughnutChart value={Noice} color={"#FFE7C8"}/>,
      text: <div className="card-text"><b>Расположение</b> - уместна ли вывеска в окружающем контексте</div>,
    },
    {
      chart:<DoughnutChart value={Place} color={"#FFD5D2"}/>,
      text: <div className="card-text"><b>Информационный шум</b> - количество информации вокруг вывески, нагруженность среды</div>,
    },
  ];

  function RenderResult() {
    const TOTALSUMMA = Style + Noice + Place;

    if (TOTALSUMMA >= 0 && TOTALSUMMA <= 10) {
      return (
        <>
          <h3 className="results__title-bad">Низкое качество логотипа</h3>
          <p className="results__description">
            Должны сообщить вам, что <b>ваша вывеска относится к разряду плохих</b>.
            Данная вывеска плохо вписывается в антураж города, и рекомендуется к
            замене в ближайшее время.
          </p>
        </>
      );
    } else if (TOTALSUMMA >= 11 && TOTALSUMMA <= 20) {
      return (
        <>
          <h3 className="results__title-normal">Среднее качество логотипа</h3>
          <p className="results__description">
            Сообщаем вам, что <b>ваша вывеска является не плохим вариантом</b>, но
            возможно, она была создана по шаблону или была выбрана из общего
            каталога<b></b>. Нет
            ничего особого или уникального, что сделало бы ее выделяющейся среди
            других вывесок.
          </p>
        </>
      );
    } else if (TOTALSUMMA >= 21) {
      return (
        <>
          <h3 className="results__title-good">Высокое качество логотипа</h3>
          <p className="results__description">
            Мы рады подтвердить, что <b>ваша вывеска отличается отличным дизайном</b>,
            четким и легко читаемыми шрифтами, привлекательными цветами и
            эффективным использованием пространства.
          </p>
        </>
      );
    } else {
      console.log("error");
    }
  }

  return (
    <div className="results">
      <Header />
      <div className="results-title">Результаты оценок</div>
      <div className="results-wrapper">
        <div className="results__picture-container">
          {/* <img src={file} alt="picture-prediction" /> */}
        </div>
        <div className="results__title-container">
          <RenderResult></RenderResult>
        </div>
      </div>
      <CardWrapper>
        {elements.map((el, index) => (
          <Card
            key={index}
            chart={el.chart}
            text={el.text}
            cardType={CardType.FIRST}
          />
        ))}
      </CardWrapper>
      <div className="results-title ">Рекомендации</div>
      <div className="results-block__wrapper">
        <img src={Icon1}/>
        <div className="results-block__wrapper__list">
          <div className="results-text1">Дизайнерское агентство «UNICORN»</div>
          <div className="results-text2">UNICORN - это креативное агентство, которое поможет вам выделиться среди конкурентов и создать уникальный брендовый образ. Мы занимаемся разработкой
            и созданием цельных и неповторимых брендовых идентичностей, которые будут отражать уникальность вашего бизнеса.
          </div>
          <Button type={ButtonType.PRIMARY} size={ButtonSize.MEDIUM} text={"Перейти >>"} onClick={handleLinkClick4}/>
        </div>
      </div>
      <div className="results-block__wrapper">
        <img className="results-icon__style" src={Icon2}/>
      <div className="results-block__wrapper__list">
        <div className="results-text1">Дизайнерское агентство «ICEBERG»</div>
        <div className="results-text2">ICEBERG - это независимое креативное агентство, которое создает интегрированные рекламные кампании с фокусом на аналитику, креатив и технологии. Агентство было создано сотрудниками с десятилетним опытом работы в ведущих международных креативных агентствах России таких, как BBDO, Instinct BBDO, Young & Rubicam.
        </div>
        <Button type={ButtonType.PRIMARY} size={ButtonSize.MEDIUM} text={"Перейти >>"} onClick={handleLinkClick5}/>
      </div>
      </div>
      <img className="results-icon__style" src={Icon3}/>
    </div>
  );
}

export default Results;
