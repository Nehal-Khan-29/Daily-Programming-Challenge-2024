def trap(h):
    if not h or len(h) < 3:
        return 0

    l, r = 0, len(h) - 1
    lmax, rmax = h[l], h[r]
    water_trapped = 0

    while l < r:
        if h[l] < h[r]:
            if h[l] < lmax:
                water_trapped += lmax - h[l]
            else:
                lmax = h[l]
            l += 1
        else:
            if h[r] < rmax:
                water_trapped += rmax - h[r]
            else:
                rmax = h[r]
            r -= 1

    return water_trapped
