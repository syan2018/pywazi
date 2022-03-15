const fs = require("fs")
const path = require("path")
const axios = require("axios")

download = async (page, tags, limit, save, key) => {
    if (!fs.existsSync(save)) {
        fs.mkdirSync(save, { recursive: true })
    }
    // Construct the url
    let url = `http://behoimi.org/post/index.json?page=${page}&tags=${tags}&limit=${limit}`
    await axios.get(url, {
        headers: {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        },
        responseType: "json"
    })
    .then(json => {
        json.data.forEach(async element => {
            await axios.get(element[key], {
                responseType: "stream",
                headers: {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "Host": "behoimi.org",
                    "Referer": url
                }
            })
            .then(res => {
                array = element[key].split("/")
                stream = fs.createWriteStream(path.join(save, `${array[array.length - 1]}`))
                res.data.pipe(stream)
            })
            .catch(err => console.log(err))
        })
    })
    .catch(err => console.log(err))
}
