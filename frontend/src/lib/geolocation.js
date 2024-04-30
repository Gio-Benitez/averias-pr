export async function getUserLocation() {
    return new Promise((resolve, reject) => {
      if (!navigator.geolocation) {
        reject(new Error("Geolocation is not supported by your browser"));
      } else {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            resolve({
              type: "Point",
              coordinates: [position.coords.longitude, position.coords.latitude],
            });
          },
          (error) => {
            reject(new Error(`Failed to retrieve location: ${error.message}`));
          }
        );
      }
    });
  }
  