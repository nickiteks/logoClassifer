import './Button.css'
import classnames from 'classnames'

export const ButtonSize = {
    SMALL: "small",
    MEDIUM: "medium",
    LARGE: "large"
}

export const ButtonType = {
    PRIMARY: "primary", 
    SECONDARY: "secondary"
}

export const Button = (props) => {

    const { size, type, text, round, onClick} = props;

    const buttonClasses = classnames (
        'button',
        type && `button-${type}`,
        size && `button-${size}`,
        `button-text__${type}`,
        { 'button-round' : round}
    )

    return(
        <div className={buttonClasses} onClick={onClick}>
            {text && <span>{text}</span>}
        </div>
    )
}