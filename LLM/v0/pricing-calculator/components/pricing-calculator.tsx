'use client'

import React, { useState, useEffect } from 'react'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

const BASE_PRICE_PER_SEAT = 10
const USAGE_PRICE_PER_UNIT = 0.5


export default function PricingCalculator() {
  const [seats, setSeats] = useState(1)
  const [usage, setUsage] = useState(0)
  const [discountTier, setDiscountTier] = useState('0')
  const [totalPrice, setTotalPrice] = useState(0)

  useEffect(() => {
    const seatCost = seats * BASE_PRICE_PER_SEAT
    const usageCost = usage * USAGE_PRICE_PER_UNIT
    const subtotal = seatCost + usageCost
    const discountPercentage = parseInt(discountTier) / 100
    const discountAmount = subtotal * discountPercentage
    const total = subtotal - discountAmount

    setTotalPrice(total)
  }, [seats, usage, discountTier])

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>SaaS Pricing Calculator</CardTitle>
        <CardDescription>Calculate your monthly bill based on seats, usage, and discounts</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="seats">Number of Seats</Label>
          <Input
            id="seats"
            type="number"
            min="1"
            value={seats}
            onChange={(e) => setSeats(Math.max(1, parseInt(e.target.value) || 1))}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="usage">Monthly Usage (units)</Label>
          <Input
            id="usage"
            type="number"
            min="0"
            value={usage}
            onChange={(e) => setUsage(Math.max(0, parseInt(e.target.value) || 0))}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="discount">Discount Tier</Label>
          <Select value={discountTier} onValueChange={setDiscountTier}>
            <SelectTrigger id="discount">
              <SelectValue placeholder="Select a discount tier" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="0">No Discount</SelectItem>
              <SelectItem value="10">10% Off</SelectItem>
              <SelectItem value="20">20% Off</SelectItem>
              <SelectItem value="30">30% Off</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </CardContent>
      <CardFooter className="flex-col items-start space-y-4">
        <div className="w-full space-y-2">
          <h3 className="text-lg font-semibold">Price Breakdown</h3>
          <div className="flex justify-between">
            <span>Seats Cost:</span>
            <span>${(seats * BASE_PRICE_PER_SEAT).toFixed(2)}</span>
          </div>
          <div className="flex justify-between">
            <span>Usage Cost:</span>
            <span>${(usage * USAGE_PRICE_PER_UNIT).toFixed(2)}</span>
          </div>
          <div className="flex justify-between">
            <span>Discount:</span>
            <span>{discountTier}%</span>
          </div>
          <div className="flex justify-between font-bold">
            <span>Total Monthly Price:</span>
            <span>${totalPrice.toFixed(2)}</span>
          </div>
        </div>
      </CardFooter>
    </Card>
  )
}

export { default as PricingCalculator } from "@/components/pricing-calculator";