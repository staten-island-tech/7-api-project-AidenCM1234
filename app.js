async function test(){
    const response = await fetch("https://api.chess.com/pub/player/hikaru")
    const data = await response.json()
    console.log(data)
}
test()