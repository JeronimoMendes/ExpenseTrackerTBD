import { Metadata } from "next";
import { getServerSession } from "next-auth";
import Link from "next/link";
import { redirect } from "next/navigation";

import { Icons } from "@/components/icons";
import authConfig from "../api/auth/[...nextauth]/authConfig";
import { LoginForm } from "./components/user-login-form";

export const metadata: Metadata = {
  title: "Login",
  description: "Login page into UoMe.",
};

export default async function LoginPage() {
  const session = await getServerSession(authConfig);

  if (session) {
    redirect('/dashboard');
  }

  return (
    <div className="relative h-screen flex-col items-center justify-center md:grid lg:max-w-none lg:grid-cols-2 lg:px-0">
      <title>Login</title>
      <div className="relative hidden h-full flex-col bg-muted p-10 text-white lg:flex dark:border-r">
        <div className="absolute inset-0 bg-zinc-900" />
        <div className="relative z-20 flex items-center text-lg font-medium">
          <Icons.logo className="mr-2 h-6 w-6" />
          UoMe
        </div>
        <div className="relative z-20 mt-auto">
          <blockquote className="space-y-2">
            <p className="text-lg">
              &ldquo;UoMe helped me not file for bankruptcy as all my friend weren&apos;t paying me back&rdquo;
            </p>
            <footer className="text-sm">Every College Student</footer>
          </blockquote>
        </div>
      </div>
      <div className="flex h-full items-center p-4 lg:p-8">
        <div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
          <div className="flex flex-col space-y-2 text-center">
            <h1 className="text-2xl font-semibold tracking-tight">
              Login into you account
            </h1>
            <p className="text-sm text-muted-foreground">
              Enter credentials below to login
            </p>
          </div>
          <LoginForm />
          <p className="px-8 text-center text-sm text-muted-foreground">
            <Link
              href="/signup"
              className="underline underline-offset-4 hover:text-primary"
            >
              Don&apos;t have an account? Sign up!
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
