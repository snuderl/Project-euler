

mapToFrac (a,b,c,d) = (cf / df,a)
  where cf = fromIntegral c
        df = fromIntegral d


cond (a,b) = a > 0.1

main = putStrLn $ show $ last $ takeWhile cond (drop 1 $ map mapToFrac (iterate f (2,1,0,1)))
---main = putStrLn $ show $ take 4 [1,2..]

isPrime x = not $ any divisible $ takeWhile notTooBig [2..] where
     divisible y = x `mod`y == 0
     notTooBig y = y*y <= x

primesGenerator :: [Integer]
primesGenerator = 2:3:primes'
  where
    1:p:candidates = [6*k+r | k <- [0..], r <- [1,5]]
    primes'        = p : filter isPrime candidates
    isPrime n      = all (not . divides n)
                       $ takeWhile (\p -> p*p <= n) primes'
    divides n p    = n `mod` p == 0

primes = take 20000 primesGenerator
isPrime1 x = elem x primes

sieve [] = []
sieve (x:xs) = x : sieve' xs (insertprime x xs PQ.empty)
  where
    insertprime p xs table = PQ.insert (p*p) (map (* p) xs) table
    sieve' [] table = []
    sieve' (x:xs) table
      | nextComposite <= x = sieve' xs (adjust table)
      | otherwise = x : sieve' xs (insertprime x xs table)
      where
        nextComposite = PQ.minKey table
        adjust table
          | n <= x = adjust (PQ.deleteMinAndInsert n' ns table)
          | otherwise = table
            where
              (n, n':ns) = PQ.minKeyValue table


--f :: (Int,Int,Int) -> (Int,Int,Int)
f (a,b,c,d) = (a+2,nums !! 3,c+primes,d+4)
  where nums = drop 1 [b,a+b..]
        primes = length $ filter isPrime1 (take 4 nums)