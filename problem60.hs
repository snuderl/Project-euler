primesGenerator :: [Integer]
primesGenerator = 2:3:primes'
  where
    1:p:candidates = [6*k+r | k <- [0..], r <- [1,5]]
    primes'        = p : filter isPrime candidates
    isPrime n      = all (not . divides n)
                       $ takeWhile (\p -> p*p <= n) primes'
    divides n p    = n `mod` p == 0

primes = primesGenerator


