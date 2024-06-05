'use client'
// import type { Metadata } from 'next';
import Header from './components/layout/header';
import Sidebar from './components/layout/sidebar';

// export const metadata: Metadata = {
//   title: 'UoMe',
//   description: 'Expense tracking app'
// };

export default function DashboardLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <Header />
      <div className="flex h-screen overflow-hidden">
        <Sidebar />
        <main className="w-full pt-16">{children}</main>
      </div>
    </>
  );
}
