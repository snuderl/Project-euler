

powers base = powers1 base 1

powers1 :: Int -> Int -> [Int]
powers1 base pow
    | len < pow && base > 1 = []
    | pow == len = 1 : powers1 base (pow + 1)
    | otherwise = 0 : powers1 base (pow + 1)
  where n = (fromIntegral base) ** (fromIntegral  pow)
        len = length $ show $ (truncate n)

main = putStrLn $ show $ 1 + (sum $ map (sum . powers) [2..9]) -- 1 is for 1^x...