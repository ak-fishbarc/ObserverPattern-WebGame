const news_one = {name: "Event", address: "someaddressforlink", image: "news_image.png"}
const news_two = {name: "Promotion", address: "someaddressforlink", image: "news_image2.png"}
const news_three = {name: "Deal", address: "someaddressforlink", image: "news_image3.png"}

const news_to_flash = [news_one, news_two, news_three]
const news_space = document.getElementById("NewestNews");

document.getElementById("NewsImage").src = `/static/${news_to_flash[0].image}`

for (let story in news_to_flash)
{
    let button = document.createElement("button");
    button.style.width = "50px";
    button.style.height = "15px";
    button.onclick = function(e){
    document.getElementById("NewsImage").src = `/static/${news_to_flash[story].image}`, false}
    news_space.appendChild(button);
}








