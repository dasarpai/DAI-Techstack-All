let mobilenet;
let video;
let label = '';

// when model is ready make predictions
function modelReady() {
    console.log('Model is ready!!!');
    mobilenet.predict(gotResults);
}

function gotResults(error, results) {
    if (error) {
        console.error(error);
    } else {
        label = results[0].className;
        // loop the inference by calling itself
        mobilenet.predict(gotResults);
    }
}

// setup function
function setup() {
    createCanvas(640, 550);
    // ml5 to create video capture
    video = createCapture(VIDEO);
    video.hide();
    background(0);
    // load the MobileNet and apply it on video feed
    mobilenet = ml5.imageClassifier('MobileNet', video, modelReady);
}

function draw() {
    background(0);
    // show video 
    image(video, 0, 0);
    fill(255);
    textSize(32);
    // show prediction label 
    text(label, 10, height - 20);
}