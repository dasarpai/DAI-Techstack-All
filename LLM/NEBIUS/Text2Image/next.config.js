/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: { unoptimized: true },
  env: {
    NEBIUS_API_KEY: process.env.NEBIUS_API_KEY,
  },
  output: 'standalone'
};

module.exports = nextConfig;