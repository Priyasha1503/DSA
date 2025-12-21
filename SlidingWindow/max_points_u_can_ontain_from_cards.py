
#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==1:
            return max(cardPoints[-1],cardPoints[0])

        lsum=sum(cardPoints[0:k])
        rsum=0
        l=k-1
        r=len(cardPoints)-1
        maxsum=lsum
        while l>=0 and r>=0:
            lsum=lsum-cardPoints[l]
            l-=1
            rsum=rsum+cardPoints[r]
            r-=1
            maxsum=max(maxsum,lsum+rsum)

        return maxsum

