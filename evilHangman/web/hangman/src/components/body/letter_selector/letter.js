function Letter(props) {

    const style = props.activated ?  {} : { backgroundColor: "#333333" }
    const onClick = props.activated ? () => {props.letterClick(props.letter)} : () => {}

    const additionalProps = {...props};

    return (
        <img src={"letters/" + props.letter.toLowerCase() + ".png"} style={style} alt={props.letter} onClick={() => {onClick()}} {...additionalProps}></img>
    );
}

export default Letter;