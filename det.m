function result = determination(matrix)
    if (size(matrix) != [2, 2])
        error("Input matrix must be a 2x2 matrix");
    end
    result = matrix(1,1) * matrix(2,2) - matrix(1,2) * matrix(2,1);
end

matrix_2 = [3, 4; 3, 4];
result = determination(matrix_2);
disp(["Determination of 2x2 matrix: ", num2str(result)]);