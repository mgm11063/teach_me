"use client";
export const config = { runtime: 'client' };
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { HiOutlineHome, HiOutlineOfficeBuilding } from "react-icons/hi";
import { LuUsers2 } from "react-icons/lu";
import { TiTag } from "react-icons/ti";
import { AiOutlineMessage } from "react-icons/ai";

const navigationItems = [
  { name: 'Home', href: '/', icon: <HiOutlineHome /> },
  { name: 'Invoices', href: '/questions', icon: <HiOutlineOfficeBuilding /> },
  { name: 'Clients', href: '/clients', icon: <LuUsers2 /> },
  { name: 'Products', href: '/products', icon: <TiTag /> },
  { name: 'Messages', href: '/messages', icon: <AiOutlineMessage /> },
  // { name: 'Settings', href: '/settings', icon: <SettingsIcon /> },
  // { name: 'Help', href: '/help', icon: <HelpIcon /> },
];

const Nav = () => {
  const pathname = usePathname();

  return (
    <nav>
      <div>
        {navigationItems.map((item) => (
          <Link href={item.href}>
            <span key={item.name} className={`flex items-center rounded-xl py-3 px-6 my-2 transition-colors duration-200 ${pathname === item.href ? ' bg-C-dark-light text-C-white' : 'text-C-white hover:bg-C-dark-light'
              }`}>
              {item.icon}
              <span className="ml-3 ">{item.name}</span>
            </span>
          </Link>
        ))}
      </div>
      {/* Logout or other items */}
    </nav>
  );
};

export default Nav;
