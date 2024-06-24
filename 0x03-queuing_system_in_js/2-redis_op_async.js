import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

client.on("error", (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

client.on("connect", () => console.log("Redis client connected to the server"));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
  const asynced = promisify(client.get).bind(client);
  const value = await asynced(schoolName);
  console.log(value);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
