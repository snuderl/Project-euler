
import Data.Char

loop = map (\ x -> maxOfList (powersOf x x 100 0)) [1..100]

maxOfList x = maximum $ map (\ k -> intToSum k) x

powersOf :: Integer -> Integer -> Integer -> Integer -> [Integer]
powersOf a current limit pos
    | pos == limit = [next]
    | otherwise = next : (powersOf a next limit (pos + 1))
  where next = current * a

intToSum :: Integer -> Int
intToSum = (sum . (map digitToInt) . show)


digits :: Integer -> Int
digits n = sum $ map (\x -> read [x] :: Int) (show n)

sumOfDigits :: Integer -> Integer -> Integer
sumOfDigits x s
  | x < 10 = x + s
  | otherwise = sumOfDigits (div x 10) (s+ (mod x 10))

main = putStrLn $ show $ maximum loop