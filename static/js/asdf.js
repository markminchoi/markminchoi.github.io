let flag = 0

const handleScrollEvent = () => {
    let ppage = document.getElementsByClassName('page-body')[0]
    if (flag) {
        let newNode = document.createElement('p')
        newNode.innerHTML = 'Oops..!'
        ppage.appendChild(newNode)
    }

    else {
        let newNode = document.createElement('p')
        let newNode2 = document.createElement('a')
        newNode.innerHTML = '💿 '
        newNode2.innerHTML = '<b>Spotify</b>'
        newNode2.href = 'https://open.spotify.com/user/iivlnkcx4glq9gurpitdf1oby'
        newNode.appendChild(newNode2)
        ppage.appendChild(newNode)
        flag++
    }
}

const throttle = (fn, delay) => {
    let timer
    return function () {
        if (!timer) {
            timer = setTimeout(() => {
                timer = null
                fn.apply(this, arguments)
            }, delay)
        }
    }
}

window.onload = function() {
    window.addEventListener('scroll', throttle(handleScrollEvent, 500))
    window.addEventListener('wheel', throttle(handleScrollEvent, 500))
    window.addEventListener('touchmove', throttle(handleScrollEvent, 500))
}