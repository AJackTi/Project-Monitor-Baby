using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using System.Linq;
using WebApplication.Controllers.api;
using WebApplication.Models;

namespace WebApplication.Controllers
{
    public class HomeController : Controller
    {
        public HomeController()
        {
        
        }
        public IActionResult Privacy()
        {
            return View();
        }

        public IActionResult Login()
        {
            //ViewBag.sessionv = HttpContext.Session.SetString("username");
            return View();
        }

        public IActionResult SignUp()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        public IActionResult Dashboard()
        {
            var aaa = LoginController.listUserSession.ToList();
            if (aaa.Any())
            {
                return View();
            }
            return RedirectToAction("ErrorPage");
        }

        public IActionResult Transform()
        {
            return View();
        }

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult ErrorPage()
        {
            return View();
        }
    }
}
