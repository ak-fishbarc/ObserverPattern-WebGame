// Get data from the server via element and parse it.
const news_to_flash = JSON.parse(document.getElementById("flash_news").getAttribute("event"))
const news_space = document.getElementById("NewestNews");
document.getElementById("NewsImage").src = `${news_to_flash[0].image}`
document.getElementById("NewsLink").href = `${news_to_flash[0].address}`

// Create buttons, links and images for each news that's on the top of the page.
// Get data from parsed JSON.
for (let story in news_to_flash)
{
    let button = document.createElement("button");
    button.style.width = "50px";
    button.style.height = "15px";

    button.onclick = function(e){
    document.getElementById("NewsLink").href = `${news_to_flash[story].address}`
    document.getElementById("NewsImage").src = `${news_to_flash[story].image}`,
    false}

    news_space.appendChild(button);
}








