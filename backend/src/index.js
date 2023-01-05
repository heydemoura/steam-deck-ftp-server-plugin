const FtpSrv = require("ftp-srv");

const port = 2121;
const ftpServer = new FtpSrv({
  url: "ftp://0.0.0.0:" + port,
  greeting: "SteamDeck FTP server started.",
  tls: true,
  anonymous: true,
});

ftpServer.on("login", ({ connection, username, password }, resolve, reject) => {
  if (username === "deck" && password === "deck") {
    resolve({
      // root: "/Users/heydemoura/",
      root: "/home/deck/",
    });
  }

  return reject(new Error("Oh no! Something went wrong."));
});

ftpServer.on("server-error", ({ error }) => {
  console.log(error);
});

ftpServer.listen().then(() => {
  console.log("SteamDeck FTP Server Running.");
});
