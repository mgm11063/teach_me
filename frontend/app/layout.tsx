import './globals.css'
import Nav from '@/components/Nav'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <div className="flex h-screen bg-gray-100">
        <aside className=" w-72 bg-C-dark px-5" aria-label="Sidebar">
          <Nav />
        </aside>
        <main className="flex-1 p-8">
          {children}
        </main>
      </div>
    </>
  )
}
