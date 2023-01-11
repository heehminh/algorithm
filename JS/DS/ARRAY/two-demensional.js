let averageTempDay = []
averageTempDay[0] = [72, 75, 79, 79, 81, 81];
averageTempDay[1] = [81, 79, 75, 75, 73, 72];

function printMatrix (myMatrix) {
    for (let i=0; i<myMatrix.length; i++) {
        myMatrixResult = "";
        for (let j=0; j<myMatrix[i].length; j++) {
            myMatrixResult += " " + myMatrix[i][j];
        }
        console.log(myMatrixResult)
    }
}

printMatrix(averageTempDay);