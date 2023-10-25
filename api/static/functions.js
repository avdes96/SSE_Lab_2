function random_fact() {
    var num = Math.floor(Math.random() * 3) + 1
    var dict = {
        1 : "Fact 1",
        2 : "Fact 2",
        3 : "Fact 3",
    }

    let output = dict[num]
    console.log(output)


    document.getElementById("fact").textContent = output;
}