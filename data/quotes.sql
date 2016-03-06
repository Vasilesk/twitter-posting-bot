-- phpMyAdmin SQL Dump

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `quotes`
--

-- --------------------------------------------------------

--
-- Структура таблицы `tweets`
--

CREATE TABLE IF NOT EXISTS `tweets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tweet` varchar(140) NOT NULL,
  `label` varchar(127) DEFAULT NULL,
  `priority` int(11) NOT NULL DEFAULT '10000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=60 ;

--
-- Дамп данных таблицы `tweets`
--

INSERT INTO `tweets` (`id`, `tweet`, `label`, `priority`) VALUES
(1, '“Train yourself to write everyday. Even if you have nothing to write, write and say so.”\n', 'favs', 10000),
(2, '“It is not enough to have a good mind; the main thing is to use it well.”\n', 'favs', 10000),
(3, '“I want to taste your lips before coffee and your skin before sunshine.”\n', 'favs', 10000),
(4, '“Damaged people are dangerous. They know how to make hell feel like home.”\n', 'favs', 10000),
(5, '“Never underestimate the power of good morning texts, apologies, and random compliments.”\n', 'favs', 10000),
(6, '"I learned that people leave. Even if they have promised a thousand times that they won’t.”\n', 'favs', 10000),
(7, '“You either say how you feel and fuck it up or say nothing and let it fuck you up instead.”\n', 'favs', 10000),
(8, '“She wasn’t bitter. She was sad, though. But it was a hopeful kind of sad. The kind of sad that just takes time. ”\n', 'favs', 10000),
(9, '“One day you will meet someone who will make this messy and hard life easier than you ever thought possible. And you will want to stay.”\n', 'favs', 10000),
(10, 'I wish people were more straight up with things.\n', 'favs', 10000),
(11, '“You have to find the right distance between people. Too close, and they overwhelm you, too far and they abandon you.”\n', 'favs', 10000),
(12, 'True love is the ability so see something in a person that no one else does.\n', 'favs', 10000),
(13, '“Sometimes all you need to do is just worry about yourself.”\n', 'favs', 10000),
(14, '"Do not spoil what you have by desiring what you have not; remember that what you now have was once among the things you only hoped for.”\n', 'favs', 10000),
(15, '“Don’t trust the things your heart tells you when it’s sad.”\n', 'favs', 10000),
(16, 'You can’t change the past, so focus on making a great future.\n', 'favs', 10000),
(17, 'Running away from your problems is a race you’ll never win.\n', 'favs', 10000),
(18, '“Looks don’t mean everything. I’d rather have a beautiful conversation than a pretty face to look at.”\n', 'favs', 10000),
(19, '“Don’t trust the things your heart tells you when it’s sad.”\n', 'favs', 10000),
(20, '“When a flower doesn’t bloom you fix the environment in which it grows, not the flower.”\n', 'favs', 10000),
(21, '“Maybe it won’t work out. But maybe seeing if it does will be the best adventure ever.”\n', 'favs', 10000),
(22, '“Be stubborn about your goals but flexible about your methods.”\n', 'favs', 10000),
(23, '"You’re not a bad person for the ways you tried to kill your sadness.”\n', 'favs', 10000),
(24, '“You’re like the rain… an old friend, with bad timing.”\n', 'favs', 10000),
(25, 'If you don’t fight for what you want, don’t cry for what you lost.\n', 'favs', 10000),
(26, '“I love like a leaky faucet or I love like a dam breaking. There is nothing in between.”\n', 'favs', 10000),
(27, '“The saddest people try their best to make people happy. They know what it’s like to feel worthless, they don’t want anyone to feel that.”\n', 'favs', 10000),
(28, '“I just want you to be happy. If that’s with me or with someone else or with nobody. I just want you to be happy.”\n', 'favs', 10000),
(29, '“No matter how far you travel, you can never get away from yourself.”\n', 'favs', 10000),
(30, '“I poured everything I had into you, and you were still empty.”\n', 'favs', 10000),
(31, '“I asked her if she believed in love, and she smiled and said it was her most elaborate method of self-harm."\n', 'favs', 10000),
(32, '“I know I’m unloveable, you don’t have to tell me.”\n', 'favs', 10000),
(33, '“I’d do it all over again, you know. I wouldn’t trade one second if it meant we were right here, in this moment.”\n', 'favs', 10000),
(34, '“You have to find the right distance between people. Too close, and they overwhelm you. Too far, and they abandon you.”\n', 'favs', 10000),
(35, '"Maybe, no matter how much you loved them, they could slip through your fingers like water, and there was nothing you could do about it.”\n', 'favs', 10000),
(36, '"I hope one day you find someone who makes flowers grow even in the saddest parts of you."\n', 'favs', 10000),
(37, '“I want to meet people with fire in them, burning through life like a forest fire, too many people die out and survive on embers.”\n', 'favs', 10000),
(38, '“Truth is I’m a fucking romantic. I’m difficult but I promise I’m not boring.”\n', 'favs', 10000),
(39, '"Sometimes your heart needs more time to accept what your mind already knows."\n', 'favs', 10000),
(40, '"But that’s love, to give away everything, to sacrifice everything, without the slightest desire to get anything in return.”\n', 'favs', 10000),
(41, 'Stay loyal to the people you love. Loyalty is everything.\n', 'favs', 10000),
(42, 'Always end the day with a positive thought; no matter how hard things were. Tomorrow is a fresh opportunity to make it better.\n', 'favs', 10000),
(43, 'Life is like a mirror. Smile at it and it smiles back at you.\n', 'favs', 10000),
(44, 'Be a good person. A good friend. Live the life you want. Follow your dreams.\n', 'favs', 10000),
(45, 'Stop overthinking. Relax and let it go.\n', 'favs', 10000),
(46, 'Pain makes you stronger. Fear makes you braver. Heartbreaks make you wiser.\n', 'favs', 10000),
(47, 'Stay loyal to the people you love. Loyalty is everything.\n', 'favs', 10000),
(48, 'Don’t rush anything. When the time is right, it’ll happen.\n', 'favs', 10000),
(49, 'Don’t stress. Do your best. Forget the rest.\n', 'favs', 10000),
(50, 'All good things are worth waiting for and worth fighting for.\n', 'favs', 10000),
(51, 'People come and go, but life is simply about seeing who cares enough to stay.\n', 'favs', 10000),
(52, 'Don’t force someone to make time for you, if they really want to, they will.\n', 'favs', 10000),
(53, 'The past is behind, learn from it. The future is ahead, prepare for it. The present is here, live it.\n', 'favs', 10000),
(54, 'Open your mind before your mouth.\n', 'favs', 10000),
(55, 'True love and loyal friends are two of the hardest things to find.\n', 'favs', 10000),
(56, 'Stay true to the people that believe in you.\n', 'favs', 10000),
(57, 'I hope manners is the next cool trend.\n', 'favs', 10000),
(58, 'The best way to avoid disappointments is to not expect anything from anyone.\n', 'favs', 10000),
(59, 'Don’t choose the better person, choose the person who makes you better.\n', 'favs', 10000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
