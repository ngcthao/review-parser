import gplay from "google-play-scraper";
import fsp from 'fs/promises';
import fs from 'fs';
import readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

const user_input = readline.createInterface({ input, output });

async function userInput() {
    const uri = await user_input.question('Please enter the google play url:')
    user_input.close();
    let url = new URL(uri)
    return url.searchParams.get("id")
}

async function fetchReviews(id) {
  try {

    let page = 1
    let token = null
    do {
      if (token == null && fs.existsSync('reviews/page1.json')) {
        fs.readFile('reviews/page1.json', function(err, data) {
          if (err) throw err;
          const reviews = JSON.parse(data).nextPaginationToken
        })
      }

      let res = await gplay.reviews({
        appId: id,
        sort: gplay.sort.RATING,
        paginate: true,
        nextPaginationToken: token 
      });

      token = res.nextPaginationToken;
      await fsp.writeFile(`reviews/page${page}.json`, JSON.stringify(res, null, 2));
      page++;
    } while (token);

    console.log("Reviews saved successfully");
  } catch (error) {
    console.log(error, "Failed to retrieve reviews.");
}};


fetchReviews(await userInput());