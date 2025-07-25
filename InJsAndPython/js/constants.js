// Need to add 'export' to make them available in other modules.

export const SERVER_IP = "127.0.0.1";
export const SERVER_PORT = 8001;
export const BASE_URL = `${SERVER_IP}:${SERVER_PORT}` ;  // => 127.0.0.1:8001 or http://localhost:8001/


// We only have these 3 type of data in our 3 json files under `res` folder.
//  res/
//      /orders.json
//      /products.json
//      /users.json
export const GET_ALL_OPTIONS = [ "users", "products", "orders" ];
export const GET_ONE_OPTION = [ "users", "products", "orders" ];