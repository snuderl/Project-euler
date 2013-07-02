primesGenerator :: [Integer]
primesGenerator = 2:3:primes'
  where
    1:p:candidates = [6*k+r | k <- [0..], r <- [1,5]]
    primes'        = p : filter isPrime candidates
    isPrime n      = all (not . divides n)
                       $ takeWhile (\p -> p*p <= n) primes'
    divides n p    = n `mod` p == 0

primes = (primesGenerator)

quotient x = (x, (fromIntegral x) / (fromIntegral nprimes))
  where nprimes = length $ takeWhile (<x) primes

totient primeCount x primes
  | x == head primes = (x, xs/(count+1),primeCount+1) : totient (primeCount + 1) (x+1) (tail primes)
  | otherwise = (x, xs/(count),primeCount) : totient (primeCount) (x+1) primes
  where count = (fromIntegral primeCount)
        xs = (fromIntegral x)


main = putStrLn $ show $ (take 10 (totient 0 2 primes))