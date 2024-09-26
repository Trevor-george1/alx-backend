import { createClient  } from "redis";

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
})
.on("error", () => {
    console.log(`Redis client not connected to the server: ${error}`);
});