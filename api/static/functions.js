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

function random_asteroid_fact() {
    num = (num + 1) % 9
    var dict = {
        0 : "Asteroids are minor planets!",
        1 : "There are about 1 million known asteroids!",
        2 : "Asteroids are mainly located in the asteroid belt!",
        3 : "Ceres is the largest asteroid!",
        4 : "The asteroid 4 Vesta is the only one visible to the naked eye!",
        5 : "Asteroid mining may be possible in the future!",
        6 : "The combined mass of all asteroids is equal to about 3% of the moon!",
        7 : "The Chicxulub crater in Mexico was caused by an asteroid impact!",
        8 : "The 30th June is International Asteroid Day!",
    }

    let output = dict[num]
    document.getElementById("fact").textContent = output;

}


function generate_table(data) {

var tableBody = document.getElementById("table_body");

for (var repo in data) {
    if (data.hasOwnProperty(repo)) {
      var entry = data[repo];
      var updated_at = entry.updated_at;
      var pushed_at = entry.pushed_at;
      var hash = entry.latest_commit.hash;
      var author = entry.latest_commit.author;
      var date = entry.latest_commit.date;
      var message = entry.latest_commit.message;
      var row = tableBody.insertRow();
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);
      var cell4 = row.insertCell(3);
      var cell5 = row.insertCell(4);
      var cell6 = row.insertCell(5);
      var cell7 = row.insertCell(6);
      cell1.innerHTML = repo;
      cell2.innerHTML = updated_at;
      cell3.innerHTML = pushed_at;
      cell4.innerHTML = hash;
      cell5.innerHTML = author;
      cell6.innerHTML = date;
      cell7.innerHTML = message;
    }
  }
}


function get_compliment() {
    document.getElementById('compliment').textContent = "Generating your compliment..."    
    fetch('/chatgpt_get_compliment', {
            method: 'POST'
        })
        .then(response => response.text())
        .then(data => {
            if (data === "An error occurred with your deployment") {
                data = "ChatGPT took long to respond, please try again!"
            }
            console.log(data)
            document.getElementById('compliment').textContent = data;
        });
}