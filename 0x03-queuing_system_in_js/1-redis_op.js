import { createClient, RedisClient  } from "redis";

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
})
.on("error", () => {
    console.log(`Redis client not connected to the server: ${error}`);
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, res) => {
        if (err)
        {
            console.log(err);
            throw err;
        }
        console.log(res);
    });
}