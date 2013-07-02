

main = putStrLn $ show $ 9999 - foldl (\ count pos -> count + (lyrchel 0 pos)) 0 [1..9999]

reverseNum :: Integer -> Integer
reverseNum num = read $ reverse $ show num

lyrchel iter num
  | iter >= 50 = 0
  | otherwise = if new == reverseNum new
                then 1
                else lyrchel (1+iter) new
  where new = num + reverseNum num
