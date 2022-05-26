const response = $('#response');
const score_board = $("#score");
let score = 0; 


setTimeout(async function(){
    $('.form').empty();
    $('.form').html('<form action="/"><button>New Game</button></form>')
    const json = JSON.stringify({'score': score})
    res = await axios.post('/top-score', json, {headers: {'Content-Type': 'application/json'}})
    console.log(res)
}, 60000)


$("form").on('submit', async function(e){
    e.preventDefault();

    const guess = $('#guess').val()

    const res = await axios.get('/guess-word', {params: {guess: guess}})
    console.log(res.data.result)
    console.log(response)
    make_response(res.data.result, guess)
})

function make_response(res, guess){
    if(res === "ok"){
        console.log('Good')
        response.removeClass('bad')
        response.addClass('good')
        response.text('Good Job')
        add_score(guess)
    } else if (res === "not-on-board" || res === "not-word"){
        console.log('Not Good')
        response.remove('good')
        response.addClass('bad')
        response.text('Sorry, but wrong')
    }
}

function add_score(guess) {
    let points = guess.length;
    score += points;
    score_board.text(`Score: ${score}`)
}