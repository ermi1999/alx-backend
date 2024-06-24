import redis from "redis";

const client = redis.createClient();

const schools = {
  portland: 50,
  seatle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const entry of Object.entries(schools)) {
  client.HSET("HolbertonSchools", entry[0], entry[1], redis.print);
}

client.HGETALL("HolbertonSchools", (err, res) => {
  console.log(res);
});
