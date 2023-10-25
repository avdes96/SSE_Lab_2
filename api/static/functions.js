num = 0;

function random_dino_fact() {
    num = (num + 1) % 10
    var dict = {
        0 : "Dinosaurs first appeared over 230 million years ago!",
        1 : "Birds are the living descendants of dinosaurs!",
        2 : "The word dinosaur was coined by Sir Richard Owen in 1842 and means \"terrible lizard\"!",
        3 : "A lot of dinosaurs were very small, measuring only 50cm!",
        4 : "Some dinosaurs were nearly 60ft tall!",
        5 : "There were over 1000 species of dinosaurs!",
        6 : "Dinosaurs went extinct over 66 million year ago!",
        7 : "Dinosaurs laid eggs!",
        8 : "Some dinosaurs had feathers!",
        9 : "Jurassic Park is a famous film featuring dinosaurs!",
    }

    let output = dict[num]
    document.getElementById("fact").textContent = output;

}
