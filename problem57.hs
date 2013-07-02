import Data.Ratio

frac :: Rational -> Int -> Rational
frac rat n
    | n == 1 = 1 + den % numer
    | otherwise = frac (2 + den % numer) (n - 1)
  where numer = numerator rat
        den = denominator rat




bigger rat
    | (length $ show a) > (length $ show b) = 1
    | otherwise = 0
  where a = numerator rat
        b = denominator rat

bigger2 :: Rational -> Int
bigger2 rat
  | (truncate   (logBase 10 (fromIntegral  a))) > (truncate  (logBase 10 (fromIntegral  b))) = 1
  | otherwise = 0
  where a = numerator rat :: Integer
        b = denominator rat :: Integer

--main = putStrLn $ show $ sum $ map (bigger . (\ k -> frac 2 k)) [1..1000]
--main = putStrLn $ show $ sum $ map bigger ((3 % 2 ) : fracs)
main = putStrLn $ show answer


fracs :: [Rational]
fracs = map (\ k -> 1 + (denominator k) % (numerator k)) (createFracs (5%2) 1000)

createFracs rat n
  | n == 1 = [expand rat]
  | otherwise = rat : createFracs (expand rat) (n-1)

expand rat = 2 + den % numer
  where numer = numerator rat
        den = denominator rat

answer = length $ filter valid expansions
 where
  valid (a,b) = f a > f b where f = length . show

expansions = take 1000 $ iterate f (3,2)
 where
  f (a,b) = (2*b + a, b+a)