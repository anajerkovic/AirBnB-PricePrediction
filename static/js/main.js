function predict() {
    const roomType = document.getElementById("room_type").value;
    const city = document.getElementById("city").value;

    const data = {
        person_capacity: Number(document.getElementById("person_capacity").value),
        bedrooms: Number(document.getElementById("bedrooms").value),
        is_weekend: Number(document.getElementById("is_weekend").value),

        host_is_superhost: document.getElementById("superhost").checked ? 1 : 0,
        biz: document.getElementById("business").checked ? 1 : 0,
        multi: document.getElementById("multi").checked ? 1 : 0,

        cleanliness_rating: Number(document.getElementById("cleanliness").value),
        guest_satisfaction_overall: 90,

        room_shared: roomType === "shared" ? 1 : 0,
        room_private: roomType === "private" ? 1 : 0,

        "room_type_Private room": roomType === "private" ? 1 : 0,
        "room_type_Shared room": roomType === "shared" ? 1 : 0,
        "room_type_Entire home/apt": roomType === "entire" ? 1 : 0,

        city_amsterdam: city === "amsterdam" ? 1 : 0,
        city_athens: city === "athens" ? 1 : 0,
        city_barcelona: city === "barcelona" ? 1 : 0,
        city_berlin: city === "berlin" ? 1 : 0,
        city_budapest: city === "budapest" ? 1 : 0,
        city_lisbon: city === "lisbon" ? 1 : 0,
        city_london: city === "london" ? 1 : 0,
        city_paris: city === "paris" ? 1 : 0,
        city_rome: city === "rome" ? 1 : 0,
        city_vienna: city === "vienna" ? 1 : 0,

        // default vrijednosti (ne pita se korisnika)
        dist: 2,
        metro_dist: 1,
        attr_index: 100,
        attr_index_norm: 10,
        rest_index: 100,
        rest_index_norm: 10,
        lng: 0,
        lat: 0
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        document.getElementById("result").innerText =
            "Predicted price: " + res.predicted_price.toFixed(2) + " €";
    })
    .catch(err => {
        document.getElementById("result").innerText = "Error predicting price.";
        console.error(err);
    });
}
